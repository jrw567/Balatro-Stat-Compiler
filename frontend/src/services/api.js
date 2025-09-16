export const uploadFile = async (previous, data) => {
    if(data.entries().next().value[1].size != 0){
        let entries = [...data.entries()]
        let file_number = entries[1][1]
        let item_type = entries[2][1]
        let response = await fetch(`https://jrw567.github.io/Balatro-Stat-Compiler/${file_number}`, {method: "POST", body: data}).then((rsp) => rsp.json());
        document.getElementById(`file${file_number}`).innerHTML = response.message;
        return getList(4, item_type)
    } else {
        document.getElementById(`file1`).innerHTML = "Please upload a Balatro save file";
        return true;
    }
}

export const removeFile = async (file_number, item_type) => {
    await fetch(`https://jrw567.github.io/Balatro-Stat-Compiler/${file_number}`, {method: "DELETE"})
    return getList(4, item_type)
}

export const toggleFile = async (status, file_number, item_type) => {
    await fetch(`https://jrw567.github.io/Balatro-Stat-Compiler/${status}/${file_number}`, {method: "PATCH"})
    return getList(4, item_type)
}

export const getList = async (file_number, item_type) => {
    return await fetch(`https://jrw567.github.io/Balatro-Stat-Compiler/get_${item_type}/${file_number}`, {method: "GET"}).then((rsp) => rsp.json());
}