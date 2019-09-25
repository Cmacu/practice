let length = 1;
let longest = "";

// BRUTE FORCE
let longestPalindrome1 = str => {
  if (str.length < length) {
    return;
  }
  if (isPalindrome(str) && str.length > length) {
    length = str.length;
    longest = str;
    return;
  }
  longestPalindrome(str.slice(0, -1));
  longestPalindrome(str.slice(1));
};

let longestPalindrome2 = str => {
  let palindrome = str.slice(0, 2);
  let reversed = reverse(str);
  for (let q1 = 0; q1 < str.length; q1++) {
    for (let q2 = q1 + palindrome.length; q2 < str.length; q2++) {
      let substr = str.slice(q1, q2);
      // console.log(substr);
      let searchStart = 0;
      while (true) {
        let indexFound = reversed.indexOf(substr, searchStart);
        if (indexFound < 0) {
          break;
        }
        if (q1 === reversed.length - substr.length - indexFound) {
          palindrome = substr;
          break;
        }
        searchStart = indexFound + 1;
      }
    }
  }

  return palindrome;
};

let findSubstring = (query, str) => {
  let length = query.length;
  let qHash = new Hash();
  for (let q = 0; q < length; q++) {
    qHash.add(query.charCodeAt(q));
  }
  let sHash = new Hash();
  for (let s = 0; s < str.length; s++) {
    sHash.add(str.charCodeAt(s));
    if (s => length) {
      sHash.remove(s - length);
    }
    if (s < length - 1) {
      continue;
    }
    if (sHash === qHash) {
      let substr = str.slice(s - length);
      if (substr === query) {
        return substr;
      }
    }
  }
};

let reverse = str =>
  str
    .split("")
    .reverse()
    .join("");

let isPalindrome = str => str === reverse(str);

// console.log(isPalindrome("tet"));

// longestPalindrome2("ahanahaikmalayalamkkmdsagasdrfteqwrqeedfasfgsdgeqwrqerqetrwqteqw");
// console.log("longest:", longest);

console.log(
  longestPalindrome2(
    "wrqeedfasfgsdgeqwrqerqetrwqteqwahanahaikmalayalamkiakmdsagasdrfteqwrqeedfasfgsdgeqwrqerqetrwqteqwahanahaikmalayalamkiakmdsagasdrfteqwrqeedfasfgsdgeqwrqerqetrwqteqwahanahaikmalayalamkiakmdsagasdrfteqwrqeedfasfgsdgeqwrqerqetrwqteqwahanahaikmalayalamkiakmdsagasdrfteqwrqeedfasfgsdgeqwrqerqetrwqteqwahanahaikmalayalamkiakmdsagasdrfteqwrqeedfasfgsdgeqwrqerqetrwqteqwahanahaikmalayalamkiakmdsagasdrfteqwrqeedfasfgsdgeqwrqerqetrwqteqwahanahaikmalayalamkiakmdsagasdrfteq"
  )
);
console.log(longestPalindrome2("cabacdfgdcaba"));
