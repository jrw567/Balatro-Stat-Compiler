function Career(props){
    if(props.list.length == 0 || props.list[0] == undefined)
        return <></>
    let list = []
    const under_regex = /_/g //matches all underscores
    const name_regex = /\b[a-z]/ //matches first letters of a word that are lowercase

    let emptyList = 0
    //will order career stats manually
    Object.keys(props.list[0]).forEach((key) =>{
        if(key == "file_name"){
            //change element
            return
        }
        let newKey = key.replace(under_regex, " ")
        while(newKey.search(name_regex) >= 0){
            newKey = newKey.replace(name_regex, char => char.toUpperCase())
        }
        if(newKey == "Rounds" && props.list[0][key] == 0)
            emptyList = 1
        list.push(newKey + ": " + props.list[0][key])
    })
    return list.map((e, index) => {
        if(emptyList)
            return
        return <p key={index} className="career">{e}</p>
    })
}
export default Career