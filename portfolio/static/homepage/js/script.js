//Comportement de la sidebar en responsive

const Open = () => {
    document.querySelector('.sidebar').classList.toggle(('left-[-300px]'))
}

//Création de la carte des coordonnées
let carte = L.map('macarte').setView([50.522482, 4.204578], 11);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(carte);

let marker = L.marker([50.477762, 4.241753], {
    draggable: false,
    title: "test",
    opacity: 0.7,
})
    .addTo(carte)
    .bindPopup("<h1 class='text-xl'>Mes coordonnées</h1> \n" +
        "<i class='bi bi-telephone-inbound-fill'>+32 499/82.81.56</i><br> \n" +
        "<i class='bi bi-envelope-open'><a href='mailto:calcagnoloic93@gmail.com'> calcagnoloic93@gmail.com</a></i><br> \n" +
        "<a href='https://www.linkedin.com/in/loic-calcagno/' target='_blank'><i class='bi bi-linkedin'></i></a> \n" +
        "<a href='https://github.com/CalcagnoLoic' target='_blank'><i class='bi bi-github'></i></a> \n" +
        "<a href='https://calcagnoloic.github.io/CV/index.html' target='_blank' ><i class='bi bi-file-earmark-person-fill'></i></a>")
    .openPopup();