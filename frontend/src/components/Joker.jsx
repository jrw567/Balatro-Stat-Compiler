function Joker(props){
    if(props.list.length == 0)
        return <></>
    let list = []
    const regex = /_/g //matches all underscores
    props.list.forEach((e) =>{
        let joker = e.name
        let count = e.count
        let wins = e.wins
        let losses = e.losses
        joker = joker.replace("j_", "")
        joker = joker.replace(joker.charAt(0), joker.charAt(0).toUpperCase())
        joker = joker.replace(regex, " ")
        list.push(joker + `: Rounds: ${count} Wins: ${wins} Losses: ${losses}`)
    })
    return list.map((e, index) => {
        return <p key={index} className="jokers">{e}</p>
    })
}
export default Joker