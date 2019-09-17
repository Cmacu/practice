function processData(input) {
  let spies = [];
  for (let i = 1; i <= input; i++) {
    spies.push(i);
  }
  spies = randomSwap(spies);
  conflicts = fixConflicts(spies);
  // printSpies(spies);
  console.log(spies.length);
  console.log(spies.join(" "));
}

function fixConflicts(spies) {
  let conflicts = [];
  for (let i = 0; i < 50000; i++) {
    conflicts = findConflicts(spies);
    // console.log(conflicts);
    if (!conflicts.length) {
      break;
    }
    for (let c = 0; c < conflicts.length; c++) {
      if (conflicts.length < 5) {
        swap(spies, conflicts[c], getRandom(spies.length));
      } else {
        swap(spies, conflicts[c], conflicts[getRandom(conflicts.length)]);
      }
    }
  }
  console.log(conflicts);
  return spies;
}

function checkPath(spies, row, height, value, increase, limit = 3) {
  // console.log("steps", height, increase);
  counter = 1;
  while (+row < spies.length && +row >= 0 && value <= spies.length && value >= 0) {
    if (value == spies[row]) {
      counter += 1;
      // console.log("found", row + 1, value);
      if (counter == limit) {
        // console.log("CONFLICT", row + 1, value);
        return true;
      }
    }
    value += +increase;
    row += +height;
  }
}

function checkDanger(spies, i) {
  // DOWN
  if (i + 1 < spies.length && Math.abs(spies[i] - spies[i + 1]) == 1) {
    return true;
  }
  if (i - 1 >= 0 && Math.abs(spies[i] - spies[i - 1]) == 1) {
    return true;
  }
  // for (let row = i + 1; row < i + (spies.length - i) / 2; row++) {
  for (let row = i + 1; row < spies.length; row++) {
    // RIGHT
    let height = row - i;
    // for (value = spies[i] + 1; value < spies[i] + (spies.length - spies[i]) / 2; value++) {
    for (let value = +spies[i] + 1; value <= spies.length; value++) {
      if (checkPath(spies, row, height, value, value - spies[i])) {
        return true;
      }
    }
    // LEFT;
    // for (let value = spies[i] - 1; value >= spies[i] / 2; value--) {
    for (let value = spies[i] - 1; value >= 0; value--) {
      if (checkPath(spies, row, height, value, value - spies[i])) {
        return true;
      }
    }
  }
  // for (let row = i - 1; row >= 0; row--) {
  //   // RIGHT
  //   let height = row - i;
  //   // for (value = spies[i] + 1; value < spies[i] + (spies.length - spies[i]) / 2; value++) {
  //   for (let value = +spies[i] + 1; value <= spies.length; value++) {
  //     if (checkPath(spies, row, height, value, value - spies[i])) {
  //       return true;
  //     }
  //   }
  //   // LEFT;
  //   // for (let value = spies[i] - 1; value >= spies[i] / 2; value--) {
  //   for (let value = spies[i] - 1; value >= 0; value--) {
  //     if (checkPath(spies, row, height, value, value - spies[i])) {
  //       return true;
  //     }
  //   }
  // }
  return false;
}

function findConflicts(spies) {
  let conflicts = [];
  for (let i = 0; i < spies.length; i++) {
    const isInDanger = checkDanger(spies, i, conflicts);
    // console.log(i + 1, "is in danger", isInDanger);
    if (isInDanger) {
      conflicts.push(i);
    }
  }
  return conflicts;
}

function create(length) {
  let spies = [];
  let max = Math.floor(length / 10);
  for (let i = 1; i <= 10; i++) {
    let x = 10;
    j = i;
    while (j <= length) {
      spies.push(j);
      j += x;
      // x++;
    }
  }

  return spies;
}

function thirdSwap(spies) {
  let counter = 2;
  for (let i = 4; i < spies.length; i += counter) {
    swap(spies, i, i + counter);
    swap(spies, i + 1, i + 1 + counter);
    counter += 2;
  }
  return spies;
}

function opositeSwap(spies) {
  const half = Math.floor(spies.length / 2);
  for (let i = 1; i <= half; i += 2) {
    swap(spies, i, half + i);
  }
  return spies;
}

function getPrimes(number) {
  primes = [2];
  for (let i = 3; i <= number; i++) {
    if (!primes.find(prime => i % prime == 0)) {
      primes.push(i);
    }
  }

  return primes;
}

function fibonachi(count) {
  fib = Array(count);
  fib[0] = 0;
  fib[1] = 1;
  for (i = 2; i <= count; i++) {
    fib[i] = (fib[i - 1] + fib[i - 2]) % count;
  }
  return fib;
}

function swap(list, a, b) {
  if (a >= list.length) {
    a = a - list.length - 1;
  }
  if (b >= list.length) {
    b = b - list.length;
  }
  // console.log(a, b);
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

function fibonachiSwap(spies) {
  const fib = fibonachi(spies.length);
  let fibCount = 3;
  for (i = 0; i < spies.length; i++) {
    if (Math.abs(spies[i] - spies[i + 1]) == 1) {
      swap(spies, i, fib[fibCount]);
      fibCount++;
    }
  }
  return spies;
}

function primeSwap(spies) {
  const primes = getPrimes(spies.length);
  let primeCount = 0;
  for (i = 0; i < spies.length; i++) {
    if (Math.abs(spies[i] - spies[i + 1]) == 1) {
      swap(spies, i, primes[primeCount]);
      primeCount++;
      if (primeCount == primes.length) {
        primeCount = 0;
      }
    }
  }
  return spies;
}

function getRandom(length) {
  return Math.floor(Math.random() * 1000) % length;
}

function randomSwap(spies) {
  let loops = 0;
  let lastSwapped = 0;
  let i = 1;
  while (lastSwapped != i) {
    // for (let i = 1; i < input - 1; i++) {
    if (Math.abs(spies[i] - spies[i + 1]) == 1) {
      swap(spies, i, getRandom(spies.length));
      lastSwapped = i;
    }
    i++;
    if (i == spies.length) {
      i = 0;
      loops++;
    }
  }
  console.log(loops);
  return spies;
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
// result = "2 4 7 1 8 11 5 3 9 6 10";
// spies = result.split(" ");
// printSpies(spies);
// console.log("conflicts", findConflicts(spies));
// console.log(spies.length);
// console.log(spies.join(" "));
// return;

processData(111);
