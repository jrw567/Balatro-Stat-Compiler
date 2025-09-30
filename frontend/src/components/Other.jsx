// component used to represent Hands, Consumables, Tarots, Planets, Spectrals, and Vouchers since they are all represented by name and count
function Other(props){
    if(props.list.length == 0 || props.list[0] == undefined)
        return <></>
    let list = []
    const under_regex = /_/g //matches all underscores
    const name_regex = /\b[a-z]/ //matches first letters of a word that are lowercase
    const hand_regex = /\B[A-Z]/ //matches all uppercase letters not on boundary

    let sortedList = props.list.toSorted((a,b) => { //sorts by count which is effectively times used
        if(a.count > b.count)
            return -1
        else if(a.count < b.count)
            return 1
        return 0
    })

    sortedList.forEach((e) =>{
        let other = e.name
        other = other.replace(under_regex, " ")
        if(props.item == "hands"){
            let index = other.search(hand_regex)
            other = other.replace(hand_regex, " " + other.charAt(index)).replace("ofa", " of a")
        }
        else {
            while(other.search(name_regex) >= 0){
                other = other.replace(name_regex, char => char.toUpperCase())
            }
        }
        e.name = other
        if(props.item != "hands"){
            let img = new Image()
            img.src = `images/consumables/${e.name}.webp`
        }
        
    })

    let pageList = []
    let minPage = 10 * (props.page - 1)
    let maxPage = 10 * props.page - 1
    for(let i = minPage; i <= maxPage; i++){
        if(sortedList[i] == null)
            continue
        pageList.push(sortedList[i])
    }
    
    if(props.item == "hands"){
        return sortedList.map((e, index) => {
            let name = sortedList[index].name
            if(sortedList[0].count == 0)
                return
            return <div key={index} className="handDisplay">
                <p className={props.item}>{`${name}`}</p>
                <span>#</span>
                <p className={"count"}>{`${sortedList[index].count.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`}</p>
            </div>
            
        })
    }
    else if(props.item == "vouchers"){
        return pageList.map((e, index) => {
            let name = pageList[index].name
            let max = sortedList[0].count
            if(max == 0)
                return
            let barHeight = pageList[index].count/max * 65
            if(index>=10)
                return
            return <div key={index} className="singleDisplay">
                <img src={`images/vouchers/${name}.webp`} alt={`Image of ${name}`} />
                <p className={props.item}>{pageList[index].count.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}</p>
                <div className="bar" style={{height: barHeight + '%', background: "rgb(255, 86, 17)"}}></div>
            </div>
        })
    } else{
        return pageList.map((e, index) => {
            let name = pageList[index].name
            let max = sortedList[0].count
            if(max == 0)
                return
            let barHeight = pageList[index].count/max * 65
            let color = ""
            if(index>=10)
                return
            if(pageList[index].type == "tarot"){
                color = "rgb(158,116,206)"
            } else if(pageList[index].type == "planet"){
                color = "rgb(0,167,202)"
            } else {
                color = "rgb(46,118,253)"
            }
            return <div key={index} className="singleDisplay">
                <img src={`images/consumables/${name}.webp`} alt={`Image of ${name}`}/>
                <p className={props.item}>{pageList[index].count.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}</p>
                <div className="bar" style={{height: barHeight + '%', background: color}}></div>
            </div>
        })
    }

    
    
}
export default Other