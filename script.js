  let vid=document.getElementById("vid");
  let max=document.getElementById("intro");
  let rkt=document.getElementById("rkt");
  let val=10*scrollY;


  rkt.style.right=val*5+'px';
  vid.addEventListener("loadedmetadata", function() {
  vid.muted = true;
  vid.playbackRate = 2;
  vid.loop = true;
  vid.play();
});

const img = document.querySelector("img");
const image = [
  { name: "p1" },
  { name: "p2" },
  { name: "p3" },
  { name: "p4" },
  { name: "p5" }
];

const loadimg = (image) => {
  const imageSource = `elements/${image.name}`;
  const imgTest = new Image();
  imgTest.src = `${imageSource}.jpg`;

  imgTest.onload = () => {
    img.src = `${imageSource}.jpg`;
  };

  imgTest.onerror = () => {
    img.src = `${imageSource}.png`;
  };
};

let imageIndex = 0;
const nextimage = () => {
  imageIndex = (imageIndex + 1) % image.length;
  loadimg(image[imageIndex]);
};

const previmage = () => {
  imageIndex = (imageIndex - 1 + image.length) % image.length;
  loadimg(image[imageIndex]);
};

const next = document.getElementById("right");
const prev = document.getElementById("left");

next.addEventListener("click", nextimage);
prev.addEventListener("click", previmage);

let search=document.getElementById("srch");
let go=document.getElementById("bton");
go.onclick=function(){
  let url ="https://www.space.com/search?searchTerm="+search.value;
  window.open(url);
  search.value=null;
}







