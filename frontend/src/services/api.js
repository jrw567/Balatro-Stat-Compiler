export const uploadFile = async data => {
    if(data.entries().next().value[1].size != 0){
        let response = await fetch("http://127.0.0.1:5000/", {method: "POST", body: data}).then((rsp) => rsp.json());
        document.getElementById("file1").innerHTML = response.message;
    } else {
        document.getElementById("file1").innerHTML = "Please upload a profile.jkr file";
    }
}