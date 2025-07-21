export const uploadFile = async data => {
    await fetch("http://127.0.0.1:5000/", {method: "POST", body: data});
}