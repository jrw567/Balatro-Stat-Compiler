function Deck(props){
    let filter1 = ""
    let filter2 = ""
    console.log(props.filter)
    if(props.list.length == 0 || props.list[0] == undefined)
        return <></>
    let list = []
    let sortedList = props.list.toSorted((a,b) => { //sorts by wins
        
        if(props.filter == "wins"){
            filter1 = a.wins
            filter2 = b.wins
        }
        else if(props.filter == "losses"){
            filter1 = a.losses
            filter2 = b.losses
        }
        else
            return <></>

        if(filter1 > filter2)
            return -1
        else if(filter1 < filter2)
            return 1
        return 0
    })

    // sortedList.forEach((e) =>{
    //     let deck = e.name
    //     let wins = e.wins
    //     let losses = e.losses
    //     deck = deck.replace(deck.charAt(0), deck.charAt(0).toUpperCase())
    //     list.push(deck + ` Deck: Wins: ${wins} Losses: ${losses}`)
    // })
    // return list.map((e, index) => {
    //     let name = e.substring(0, e.indexOf(":"))
    //     return <>
    //         <p key={index} className="decks">{e}</p>
    //         <img src={`../images/decks/${name}.webp`} alt={`Image of ${name}`} />
    //     </>
    // })






    sortedList.forEach((e) =>{
        let deck = e.name
        e.name = deck.replace(deck.charAt(0), deck.charAt(0).toUpperCase())
        if(!e.name.includes("Deck"))
            e.name = e.name + " " + "Deck"
    })
    let pageList = []
    let minPage = 10 * (props.page - 1)
    let maxPage = 10 * props.page - 1
    for(let i = minPage; i <= maxPage; i++){
        if(sortedList[i] == null)
            continue
        pageList.push(sortedList[i])
    }
    return pageList.map((e, index) => {
        let max = ""
        let displayValue = ""
        let barHeight = ""
        let name = pageList[index].name
        if(props.filter == "wins"){
            max = sortedList[0].wins
            barHeight = pageList[index].wins/max * 65
            displayValue = pageList[index].wins
        }  
        else if(props.filter == "losses"){
            max = sortedList[0].losses
            barHeight = pageList[index].losses/max * 65
            displayValue = pageList[index].losses
        } 
        else
            return <></>
        if(max == 0)
            return
        
        if(index>=10) //remove and replace with proper page logic
            return
        return <div key={index} className="singleDisplay">
            <img src={`../images/decks/${name}.webp`} alt={`Image of ${name}`}/>
            {/* <p className="decks">{`${name}: Wins: ${pageList[index].wins} Losses: ${pageList[index].losses}`}</p> */}
            <p className="decks">{displayValue}</p>
            <div className="bar" style={{height: barHeight + '%', background: "rgb(95, 126, 133)"}}></div>
        </div>
    })
}
export default Deck