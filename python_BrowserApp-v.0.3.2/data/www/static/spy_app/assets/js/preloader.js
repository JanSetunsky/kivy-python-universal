function sleep(milliseconds) {  
    return new Promise(resolve => setTimeout(resolve, milliseconds));
}
function changePath (path) {
    return window.location.pathname = path
}
async function preloader() {
    document.getElementById("preloader-progress").style.width = '1%';
    for (let i = 1; i <=100 ; i++) {
        await sleep(50);
        document.getElementById("preloader-progress").style.width = i+'%';
        if(i === 100){
            window.location.assign("http://localhost:5000/spy_app/home");
        }
    }  
}
preloader();