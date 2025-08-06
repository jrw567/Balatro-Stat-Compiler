function Career(props){
    if(props.list.length == 0)
        return <></>
    let list = []
    const under_regex = /_/g //matches all underscores
    const name_regex = /\b[a-z]/ //matches first letters of a word that are lowercase
    //will order career stats manually
    Object.keys(props.list[0]).forEach((key) =>{
        if(key == "file_name"){
            //change element
            return
        }
        let new_key = key.replace(under_regex, " ")
        while(new_key.search(name_regex) >= 0){
            new_key = new_key.replace(name_regex, char => char.toUpperCase())
        }
        list.push(new_key + ": " + props.list[0][key])
    })
    return list.map((e, index) => {
        return <p key={index} className="career">{e}</p>
    })
}
export default Career