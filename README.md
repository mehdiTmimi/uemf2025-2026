# JavaScript – Documentation (à partir de `notes.txt`)

Ce document résume et illustre les points notés dans `notes.txt` avec des exemples pratiques.

## 1) Variables et types
- Portée et usage:
  - `var` → portée de fonction (à éviter, peut « fuir » au scope global)
  - `let` → portée de bloc (souvent utilisé)
  - `const` → constante (convention: MAJUSCULES pour des constantes symboliques)
- Types principaux: `number`, `string`, `boolean`, `object`, `function`.

Exemples:
```javascript
// Déclaration
let x = 42;         // number
x = "hello";        // JS est dynamique, le type peut changer

const PI = 3.14159; // constante
// PI = 3; // ❌ TypeError: Assignment to constant variable.

var old = true;     // à éviter en général
```

Bonnes pratiques:
- Préférer `const` par défaut, puis `let` si réassignation nécessaire.
- Éviter `var` et le scope global.

---

## 2) Tests (conditions)
Syntaxe similaire à C/Java. Utiliser l’égalité stricte `===` et `!==`.

```javascript
const n = 5;

if (n === 5) {
  console.log("n vaut 5");
} else if (n > 5) {
  console.log("n est grand");
} else {
  console.log("n est petit");
}
```

---

## 3) Boucles: `for`, `while`, `do...while`

```javascript
// for
for (let i = 1; i <= 10; i++) {
  console.log(i);
}

// while
let i = 1;
while (i <= 3) {
  console.log("while:", i);
  i++;
}

// do...while (s’exécute au moins une fois)
let j = 0;
do {
  console.log("do...while:", j);
  j++;
} while (j < 2);
```

---

## 4) Fonctions
Syntaxe:
```javascript
function nom(params) {
  // corps
}
```

Points clés:
- Une fonction retourne `undefined` si aucun `return` explicite n’est présent.
- Pas de surcharge (pas plusieurs fonctions avec le même nom et des signatures différentes).
- Valeurs par défaut supportées.
- Objet spécial `arguments` (semblable à un tableau) disponible en fonction classique.
- « Rest parameter » `...param` pour capturer le reste des arguments dans un vrai tableau.

Exemples:
```javascript
// Valeurs par défaut
function greet(name = "World") {
  return `Hello, ${name}!`;
}
console.log(greet());      // Hello, World!
console.log(greet("JS")); // Hello, JS!

// arguments (fonction classique uniquement)
function sumLegacy() {
  let total = 0;
  for (let i = 0; i < arguments.length; i++) total += arguments[i];
  return total;
}
console.log(sumLegacy(1, 2, 3)); // 6

// Rest parameter (recommandé)
function sum(...nums) {
  return nums.reduce((acc, n) => acc + n, 0);
}
console.log(sum(1, 2, 3, 4)); // 10

// Rest doit être le dernier paramètre
function tag(prefix, ...parts) {
  return prefix + parts.join("-");
}
console.log(tag("id:", "a", "b", "c")); // id:a-b-c
```

---

## 5) Callbacks (fonctions passées en paramètres)
Permettent la délégation et la personnalisation du comportement.

Exemple inspiré de `notes.txt` (adapté pour console):
```javascript
function randomNumber() {
  return Math.floor(Math.random() * 10); // 0..9
}

function devinette(nbr, onSuccess, onError) {
  const aleatoire = randomNumber();
  console.log("Tirage:", aleatoire);
  if (aleatoire === nbr) onSuccess();
  else onError();
}

// Avec fonctions anonymes
devinette(
  4,
  function () { console.log("bravo tu as gagné"); },
  function () { console.error("échec"); }
);

// Avec fonctions fléchées
devinette(
  4,
  () => console.log("bravo tu as gagné"),
  () => console.error("désolé !!")
);
```



## Mini‑exercices
1) Écrire une fonction `max3(a, b, c = 0)` qui retourne le maximum des trois nombres, avec `c` par défaut.
2) Écrire une fonction `avg(...nums)` qui retourne la moyenne des nombres passés.

