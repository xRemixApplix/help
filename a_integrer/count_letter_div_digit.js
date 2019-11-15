//Fonction comptant les lettres dans un texte et retournant l'arrondi de la division du nombre de lettre avec la longueur du texte
let s="H3llO W0rld!";
console.log(Math.round(s.match(/[a-zA-Z]/g).length/s.match(/\d/g).length))