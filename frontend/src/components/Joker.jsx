function Joker(props){
    if(props.list.length == 0)
        return <></>
    let list = []
    const under_regex = /_/g //matches all underscores
    const name_regex = /\b[a-z]/ //matches first letters of a word that are lowercase
    props.list.forEach((e) =>{
        let joker = e.name
        let count = e.count
        let wins = e.wins
        let losses = e.losses
        joker = joker.replace(under_regex, " ")
        while(joker.search(name_regex) >= 0){
            joker = joker.replace(name_regex, char => char.toUpperCase())
        }
        joker = joker.replace(" The ", " the ")
        joker = joker.replace(" In ", " in ")
        list.push(joker + `: Rounds: ${count} Wins: ${wins} Losses: ${losses}`)
    })
    return list.map((e, index) => {
        return <p key={index} className="jokers">{e}</p>
    })
}
export default Joker