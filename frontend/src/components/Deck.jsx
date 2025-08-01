function Deck(props){
    if(props.list.length == 0)
        return <></>
    let list = []
    console.log(props.list)
    props.list.forEach((e) =>{
        let deck = e.name
        let wins = e.wins
        let losses = e.losses
        deck = deck.replace("b_", "")
        deck = deck.replace(deck.charAt(0), deck.charAt(0).toUpperCase())
        list.push(deck + ` Deck: Wins: ${wins} Losses: ${losses}`)
    })
    return list.map((e, index) => {
        return <p key={index} className="decks">{e}</p>
    })
}
export default Deck