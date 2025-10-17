const T = [10, -23, -31, 40, -50, 66]
// T.forEach((value,index)=>{
//     console.log(value,index)
// })

// let results = T.map((ele, index) => {
//     if (ele % 2 == 0)
//         return ele +" pair"
//     return ele + " impair"
// })
// console.log(results)
const results  = T.filter((ele)=>{
    if(ele>0)
        return true
    return false
});
const results2  = T.filter(ele=>ele>0);
T[0] = 100
console.log(results)
console.log(results2)
T.sort
let numbers = [4, 2, 5, 1, 3];
numbers.sort(function(a, b) {
    console.log(a,b,a-b)
    return b - a;
});
console.log(numbers); // Affiche [1, 2, 3, 4, 5]
const persons =[
    {name:"mehdi",age:30},
    {name:"sara",age:25},
    {name:"ali",age:35}
]
persons.sort((a,b)=>{
    return a.age - b.age // name
})
console.table(persons)
// numbers.sort((a,b)=>b-a)
// console.log(numbers); // Affiche [5, 4, 3, 2, 1]
// let somme = T.reduce((acc, ele) => acc + ele, 0)

