const toBase64 = file => new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = reject;
  });


const url = '/sendVideo';

let videoName
document.getElementById('videoFile').onchange = function () {
    videoName = this.value
};

async function workWithVideo(){

    document.getElementById("Result").style.display = "block";

    let image = document.getElementById("content")
    image.src = "../css/images/load.gif"
    image.style.width = "64px"
    image.style.height = "64px"


    if(document.getElementById("videoFile").files[0]=== undefined){
      alert("Вы не выбрали видео")
      return
    }

    //let pattern = /((?:.(?!\(\d+\)))+.)(?:\(\d+\))?\..+/
    //let videoName
    //document.getElementById("videoFile").onchange = function(){
    //let videoName
    //}
    
    //console.log(videoName)
    let videoFile = document.getElementById("videoFile").files[0]
    let res_video = await toBase64(videoFile)
    let slv = res_video.split(",")
  
    var dataObj = {
      type : slv[0],
      b64 : slv[1],
      name : videoName
    }
    
    var json = JSON.stringify(dataObj);
    //console.log(json)
    requestVideo(json)
}

function requestVideo(json){
    // Формируем запрос
    response = fetch(url, {
        // Метод, если не указывать, будет использоваться GET
        method: 'POST',
        // Заголовок запроса
        headers: {
        'Content-Type': 'text/html'
        },
        // Данные
        body: json
    })
    .then((resp) => resp.json())
    .then((data)=> showClass(data)
    );
}
function showClass(data){
    let p = document.getElementById("result")
    p.textContent = data["class"]
    console.log(data)
    let image = document.getElementById("content")
    image.src = data["b64"]
    image.style.width = "100%"
    image.style.height = "100%"

    //wait(5000)
    //location. reload()
    //document.getElementById("sendVideo").remove();
    
}
function wait(ms) {
    let current_date = Date.now();
    while (current_date + ms > Date.now()) {}
}
  
async function getBD(){
    document.getElementById("BDResult").style.display = "block";
    let response = await fetch("/data");
    let str
    if (response.ok) { // если HTTP-статус в диапазоне 200-299
        // получаем тело ответа (см. про этот метод ниже)
        str = await response.text();
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
    subString = "C:\\fakepath\\"
    str = str.replace(subString, '')
    str = str.replace('$','_ _ _')
    str = str.replace('|','\n')
    document.getElementById("bd").textContent = str
    
    
    //console.log(str)
}