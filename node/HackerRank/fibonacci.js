// Return a memoizing version of a function f
var memoize = f => {
  if (!(f instanceof Function)) return f;
  if (f.length != 1) return f;

  var fn = x => {
    if (fn.memoizer.values[x] == null) {
      fn.memoizer.values[x] = f.call(f, x);
    }
    return fn.memoizer.values[x];
  };
  fn.memoizer = { values: [] };
  return fn;
};

// Function.prototype.memoize = () => {
//   if (this.length != 1) return this;
//   var _this = this;
//   var _caller = this.caller;
//   if (this.memoizer == null) {
//     this.memoizer = {
//       fn: function(x) {
//         if (_this.memoizer.values[x] == null) {
//           _this.memoizer.values[x] = _this.call(_caller, x);
//         }
//         return _this.memoizer.values[x];
//       },
//       values: []
//     };
//   }
//   return this.memoizer.fn.wrap(this);
// };

// Wrap an object, pulling wrapped object properties up to wrapper
// so as to make them accessible
// Object.prototype.wrap = function(o) {
//   for (var p in o) {
//     if (o.hasOwnProperty(p)) {
//       this[p] = o[p];
//     }
//   }
//   return this;
// };

var fibonacci = idx => {
  if (idx == 0) return 0;
  if (idx == 1) return 1;
  return fn(idx - 2) + fn(idx - 1);
};

var fn = memoize(fibonacci);

console.log(fn(35));
console.log(fn);
