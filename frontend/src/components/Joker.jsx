function Joker(props){
    let filter1 = ""
    let filter2 = ""
    if(props.list.length == 0 || props.list[0] == undefined)
        return <></>
    let list = []
    const under_regex = /_/g //matches all underscores
    const name_regex = /\b[a-z]/ //matches first letters of a word that are lowercase

    let sortedList = props.list.toSorted((a,b) => { //sorts by rounds played
        if(props.filter == "count"){
            filter1 = a.count
            filter2 = b.count
        }
        else if(props.filter == "wins"){
            filter1 = a.wins
            filter2 = b.wins
        }
        else if(props.filter == "losses"){
            filter1 = a.losses
            filter2 = b.losses
        }
        else
            return

        if(filter1 > filter2)
            return -1
        else if(filter1 < filter2)
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
        joker = joker.replace(under_regex, " ")
        while(joker.search(name_regex) >= 0){
            joker = joker.replace(name_regex, char => char.toUpperCase())
        }
        joker = joker.replace(" The ", " the ")
        joker = joker.replace(" In", "-In")
        e.name = joker
        let img = new Image()
        img.src = `../images/jokers/${e.name}.webp`
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
        if(props.filter == "count"){
            max = sortedList[0].count
            barHeight = pageList[index].count/max * 65
            displayValue = pageList[index].count
        }
        else if(props.filter == "wins"){
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
            return
        if(max == 0)
            return
        
        if(index>=10) //remove and replace with proper page logic
            return
        return <div key={index} className="singleDisplay">
            <img src={`../images/jokers/${name}.webp`} alt={`Image of ${name}`}/>
            {/* <p className="jokers">{`${name}: Rounds: ${pageList[index].count} Wins: ${pageList[index].wins} Losses: ${pageList[index].losses}`}</p> */}
            <p className="jokers">{displayValue}</p>
            <div className="bar" style={{height: barHeight + '%', background: "rgb(95, 126, 133)"}}></div>
        </div>
    })


}
export default Joker