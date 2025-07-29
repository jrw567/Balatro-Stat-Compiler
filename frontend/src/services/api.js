export const uploadFile = async (previous, data) => {
    if(data.entries().next().value[1].size != 0){
        let entries = [...data.entries()]
        let file_number = entries[1][1]
        let item_type = entries[2][1]
        let response = await fetch(`http://127.0.0.1:5000/upload_file/${file_number}`, {method: "POST", body: data}).then((rsp) => rsp.json());
        document.getElementById(`file${file_number}`).innerHTML = response.message;
        return getList(file_number, item_type) //will want to change this to file_number 4
    } else {
        document.getElementById(`file1`).innerHTML = "Please upload a profile.jkr file";
        return true;
    }
}

export const removeFile = async file_number => {
    await fetch(`http://127.0.0.1:5000/remove_file/${file_number}`, {method: "DELETE"})
}

export const getList = async (file_number, item_type) => {
    return await fetch(`http://127.0.0.1:5000/get_${item_type}/${file_number}`, {method: "GET"}).then((rsp) => rsp.json());
}