function Joker(props){
    if(props.list.length == 0)
        return <></>
    let list = []
    const under_regex = /_/g //matches all underscores
    const name_regex = /\b[a-z]/ //matches first letters of a word that are lowercase

    let sortedList = props.list.toSorted((a,b) => { //sorts by rounds played
        if(a.count > b.count)
            return -1
        else if(a.count < b.count)
            return 1
        return 0
    })
    
    sortedList.forEach((e) =>{
        let joker = e.name
        let count = e.count
        let wins = e.wins
        let losses = e.losses
        joker = joker.replace(under_regex, " ")
        while(joker.search(name_regex) >= 0){
            joker = joker.replace(name_regex, char => char.toUpperCase())
        }
        joker = joker.replace(" The ", " the ")
        joker = joker.replace(" In", "-In")
        list.push(joker + `: Rounds: ${count} Wins: ${wins} Losses: ${losses}`)
    })
    return list.map((e, index) => {
        let name = e.substring(0, e.indexOf(":"))
        let filePath = "../images/jokers/" + name + ".webp"
        console.log(filePath)
        return <>
            <p key={index} className="jokers">{e}</p>
            <img src={filePath} alt="" />
        </>
    })
}
export default Joker