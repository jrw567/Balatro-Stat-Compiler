export const uploadFile1 = async data => {
    if(data.entries().next().value[1].size != 0){
        let response = await fetch(`http://127.0.0.1:5000/upload_file/1`, {method: "POST", body: data}).then((rsp) => rsp.json());
        document.getElementById("file1").innerHTML = response.message;
    } else {
        document.getElementById("file1").innerHTML = "Please upload a profile.jkr file";
    }
}

export const uploadFile2 = async data => {
    if(data.entries().next().value[1].size != 0){
        let response = await fetch(`http://127.0.0.1:5000/upload_file/2`, {method: "POST", body: data}).then((rsp) => rsp.json());
        document.getElementById("file2").innerHTML = response.message;
    } else {
        document.getElementById("file2").innerHTML = "Please upload a profile.jkr file";
    }
}

export const uploadFile3 = async data => {
    if(data.entries().next().value[1].size != 0){
        let response = await fetch(`http://127.0.0.1:5000/upload_file/3`, {method: "POST", body: data}).then((rsp) => rsp.json());
        document.getElementById("file3").innerHTML = response.message;
    } else {
        document.getElementById("file3").innerHTML = "Please upload a profile.jkr file";
    }
}