function Deck(props){
    if(props.list.length == 0)
        return <></>
    let list = []
    let sortedList = props.list.toSorted((a,b) => { //sorts by wins
        if(a.wins > b.wins)
            return -1
        else if(a.wins < b.wins)
            return 1
        return 0
    })

    sortedList.forEach((e) =>{
        let deck = e.name
        let wins = e.wins
        let losses = e.losses
        deck = deck.replace(deck.charAt(0), deck.charAt(0).toUpperCase())
        list.push(deck + ` Deck: Wins: ${wins} Losses: ${losses}`)
    })
    return list.map((e, index) => {
        return <p key={index} className="decks">{e}</p>
    })
}
export default Deck