function Career(props){
    if(props.list.length == 0 || props.list[0] == undefined)
        return <></>
    let list = []
    let keyList = []
    const under_regex = /_/g //matches all underscores
    const name_regex = /\b[a-z]/ //matches first letters of a word that are lowercase

    let emptyList = 0

    keyList.push("wins")
    keyList.push("losses")
    keyList.push("rounds")
    keyList.push("hands_played")
    keyList.push("cards_played")
    keyList.push("cards_discarded")
    keyList.push("face_cards_played")
    keyList.push("shop_rerolls")
    keyList.push("dollars_earned")
    keyList.push("shop_dollars_spent")
    keyList.push("tarot_reading_used")
    keyList.push("tarots_bought")
    keyList.push("planets_used")
    keyList.push("planets_bought")
    keyList.push("jokers_sold")
    keyList.push("vouchers_bought")
    keyList.push("playing_cards_bought")

    keyList.forEach((key) =>{
        console.log(key)
        if(key == "file_name"){
            return
        }
        let newKey = key.replace(under_regex, " ")
        while(newKey.search(name_regex) >= 0){
            newKey = newKey.replace(name_regex, char => char.toUpperCase())
            if(newKey == "Rounds")
                newKey = "Rounds Played"
            if(newKey == "Shop Dollars Spent")
                newKey = "Dollars Spent"
            if(newKey == "Tarot Reading Used")
                newKey = "Tarots Used"
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
                <p className={"count"}>{`${count.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`}</p>
            </div>
    })
}
export default Career