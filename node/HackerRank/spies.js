function processData(input) {
  let spies = [];
  for (let i = 1; i <= input; i++) {
    spies.push(i);
  }
  spies = randomSwap(spies);
  conflicts = fixConflicts(spies);
  printSpies(spies);
  console.log(spies.length);
  console.log(spies.join(" "));
}

function fixConflicts(spies) {
  let conflicts = findConflicts(spies, true);
  let best = conflicts.length;
  let bestEver = conflicts.length;
  let pairs = {};
  for (let t = 0; t < 5000; t++) {
    if (!conflicts.length) {
      break;
    }
    let pair = conflicts.join("_");
    if (pairs.hasOwnProperty(pair)) {
      pairs[pair]++;
      for (let p = 0; p < pairs[pair]; p++) {
        swap(spies, getRandom(spies.length), getRandom(spies.length));
      }
      conflicts = findConflicts(spies, true);
      best = conflicts.length;
    } else {
      pairs[pair] = 1;
    }
    conflicts = randomSwap(conflicts);
    for (let c = 0; c < conflicts.length; c++) {
      let conflict = conflicts[c];
      let bestSpy = getRandom(spies.length);
      let bestLength = conflicts.length;
      for (let s = 0; s < spies.length; s++) {
        if (conflict == s || conflict == bestSpy) {
          continue;
        }
        swap(spies, conflict, s);
        let thisConflicts = findConflicts(spies);
        if (thisConflicts.length < bestLength) {
          bestLength = thisConflicts.length;
          bestSpy = s;
        }
        swap(spies, conflict, s);
      }
      if (bestLength < bestEver) {
        bestEver = bestLength;
        console.log(bestEver);
      }
      if (bestLength < best) {
        best = bestLength;
        swap(spies, conflict, bestSpy);
        break;
      }
    }
    conflicts = findConflicts(spies);
    // printSpies(spies);
    // console.log(best, conflicts.length, conflicts);
    console.log();
  }
  // console.log(pairs);
  console.log(conflicts);
  return spies;
}

function findConflicts(spies, fix = false) {
  let conflicts = [];
  for (let i = 0; i < spies.length; i++) {
    if (conflicts.find(c => c == i)) {
      continue;
    }
    let inDanger = isInDanger(spies, i);
    if (inDanger) {
      if (!fix) {
        conflicts.push(i);
        continue;
      }
      for (j = 0; j < conflicts.length; j++) {
        const c = conflicts[j];
        swap(spies, i, c);
        if (isInDanger(spies, i) || isInDanger(spies, c)) {
          swap(spies, i, c);
        } else {
          inDanger = false;
          conflicts = conflicts.filter(t => t != c);
          break;
        }
      }
      if (inDanger) {
        conflicts.push(i);
      }
    }
  }
  return conflicts;
}

function isInDanger(spies, i) {
  let angles = {};
  for (let j = 0; j < spies.length; j++) {
    let corner = Math.abs(j - i);
    if (corner > 0 && corner == Math.abs(spies[j] - spies[i])) {
      // printSpies(spies);
      // console.log(i + 1, "is diagonal of ", j + 1);
      return true;
    }
    let angle = Math.atan2(spies[j] - spies[i], j - i);
    // console.log(angle);
    if (angles.hasOwnProperty(angle)) {
      // console.log(i + 1, "is line with ", j + 1, " and ", angles[angle] + 1);
      return true;
    }
    angles[angle] = j;
  }

  return false;
}

function swap(list, a, b) {
  const temp = list[a];
  list[a] = list[b];
  list[b] = temp;
}

function printSpies(spies) {
  const len = spies.length;
  // console.log(spies);
  for (let i = 0; i < len; i++) {
    const row = [(i + 1).pad(3)];
    for (let j = 1; j <= len; j++) {
      row.push(j == spies[i] ? "*" : ".");
    }
    console.log(row.join(" "));
  }
}

function getRandom(length) {
  return Math.floor(Math.random() * 1000) % length;
}

function randomSwap(list) {
  for (let r = 0; r < 10; r++) {
    for (let i = 0; i < list.length; i++) {
      swap(list, i, getRandom(list.length));
    }
  }
  return list;
}

Number.prototype.pad = function(size) {
  var s = String(this);
  while (s.length < (size || 2)) {
    s = "0" + s;
  }
  return s;
};

// result = "3 21 2 14 12 15 17 5 18 7 9 20 16 4 11 6 13 10 22 1 19 8 23"
// result = "16 26 4 24 28 9 17 15 10 32 11 21 19 2 20 25 13 3 8 6 29 7 14 30 27 1 23 12 5 18 33 22 31";
// result = "1 4 8 6 3 5 2 7 9";
// result = "2 4 7 1 8 11 5 3 9 6 10";
// result = "2 4 1 5 3";
// result = "9 7 2 4 15 12 1 5 17 6 13 10 8 11 16 3 14";
// result = "15 18 12 21 8 4 2 10 22 20 1 9 6 13 19 16 11 23 5 3 17 7 14";
// spies = result.split(" ");
// printSpies(spies);
// console.log("conflicts", findConflicts(spies));
// console.log(spies.length);
// console.log(spies.join(" "));
// return;

processData(99);
