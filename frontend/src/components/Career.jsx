function Career(props){
    if(props.list.length == 0 || props.list[0] == undefined)
        return <></>
    let list = []
    const under_regex = /_/g //matches all underscores
    const name_regex = /\b[a-z]/ //matches first letters of a word that are lowercase

    let emptyList = 0
    Object.keys(props.list[0]).forEach((key) =>{
        let newKey = key.replace(under_regex, " ")
        while(newKey.search(name_regex) >= 0){
            newKey = newKey.replace(name_regex, char => char.toUpperCase())
        }
        if(newKey == "Rounds" && props.list[0][key] == 0)
            emptyList = 1
        list.push(newKey + ": " + props.list[0][key])
    })
    return list.map((e, index) => {
        let name = e.substring(0, e.indexOf(":"))
        let count = e.substring(e.indexOf(":") + 2, e.length)
        let str = "#"
        if(name.includes("Dollar"))
            str = "$"
        if(emptyList)
            return
        return <div key={index} className="careerDisplay">
                <p className={props.item}>{`${name}`}</p>
                <span>{str}</span>
                <p className={"count"}>{`${count}`}</p>
            </div>
    })
}
export default Career