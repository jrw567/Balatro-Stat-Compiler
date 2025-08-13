import "../css/Joker.css"

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
    
    // sortedList.forEach((e) =>{
    //     let joker = e.name
    //     let count = e.count
    //     let wins = e.wins
    //     let losses = e.losses
    //     joker = joker.replace(under_regex, " ")
    //     while(joker.search(name_regex) >= 0){
    //         joker = joker.replace(name_regex, char => char.toUpperCase())
    //     }
    //     joker = joker.replace(" The ", " the ")
    //     joker = joker.replace(" In", "-In")
    //     list.push(joker + `: Rounds: ${count} Wins: ${wins} Losses: ${losses}`)
    // })
    // return list.map((e, index) => {
    //     if(index>=10) //remove and replace with proper page logic
    //         return
    //     let name = e.substring(0, e.indexOf(":"))
    //     return <div className="joker">
    //         <img src={`../images/jokers/${name}.webp`} alt={`Image of ${name}`} />
    //         <p key={index} className="jokers">{e}</p>
    //         <div ></div>
    //     </div>
    // })


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
        e.name = joker
    })
    return sortedList.map((e, index) => {
        let max = sortedList[0].count
        let barHeight = sortedList[index].count/max * 65
        if(index>=10) //remove and replace with proper page logic
            return
        let name = sortedList[index].name
        return <div key={index} className="joker">
            <img src={`../images/jokers/${name}.webp`} alt={`Image of ${name}`} />
            <p className="jokers">{`${name}: Rounds: ${sortedList[index].count} Wins: ${sortedList[index].wins} Losses: ${sortedList[index].losses}`}</p>
            <div className="bar" style={{height: barHeight + '%'}}></div>
        </div>
    })


}
export default Joker