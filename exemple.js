function Person(name, age) {
    this.x = name; // public String x = name
    this.y = age;
    let x = name; // private String x = name
    this.sePresenter = function() {
        console.log("1 - Je m'appelle " + this.x + " et j'ai " + this.y + " ans.");
    }
    this.sePresenter2 = function() {
        console.log("2 - Je m'appelle " + x + " et j'ai " + this.y + " ans.");
    }
}
let personne1 = new Person("Alice", 30);
console.log(personne1); // Affiche "Alice"
personne1.sePresenter2();

let Etudiant = (name)=>{
    this.name = name
    console.log(this.name)
}
let etudiant = new Etudiant("mehdi");