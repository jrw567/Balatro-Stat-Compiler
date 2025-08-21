import Career from "./Career"
import Deck from "./Deck"
import Joker from "./Joker"
import Other from "./Other"
import "../css/DisplayList.css"
import { useState, useEffect } from "react"

function DisplayList(props){
    const [page, setPage] = useState(1)
    const [filter, setFilter] = useState("") //need to have key updated and also need to properly update filter

    let pageLimit = 0
    if(props.item == "decks" || props.item == "planets" || props.item == "spectrals")
            pageLimit = 2
        else if(props.item == "jokers")
            pageLimit = 15
        else if(props.item == "consumables")
            pageLimit = 6
        else if(props.item == "tarots")
            pageLimit = 3
        else if(props.item == "vouchers")
            pageLimit = 4
        else
            pageLimit = 1

    useEffect (() => {
        if(props.item == "deck")
            setFilter("wins")
        else if(props.item == "jokers")
            setFilter("count")
        setPage(1)
  }, [props.item])

    function decrementPage(){
        if(page > 1)
            setPage(page - 1)
    }

    function incrementPage(){
        
        if(page < pageLimit) //change to variable dependant on props.item****************
            setPage(page + 1)
    }
    if(props.list == null || props.item == null || props.list.length == 0)
        return <div id="displayBox">
            <p>Insert description of how the application works</p>
        </div>
    if(props.item == "career")
        return <div id="displayBox"><Career list={props.list}/></div>
    else if(props.item == "decks")
        return <>
            <div id="displayBox">
                <div className="key">
                        <div></div>
                        <span>Total wins with this deck</span>
                </div>
                <div className="filter">
                        <button onClick={() => {setFilter("wins")}}>Wins</button>
                        <button onClick={() => {setFilter("losses")}}>Losses</button>
                </div>
                <Deck list={props.list} page={page}  filter={filter}/>
                </div>
            <div id='page'>
                    <button onClick={() => {decrementPage()}}>&lt;</button>
                    <span>{`Page ${page}/${pageLimit}`}</span>
                    <button onClick={() => {incrementPage()}}>&gt;</button>
            </div>
        </> 
    else if(props.item == "jokers")
        return <>
                <div id="displayBox">
                    <div className="key">
                        <div></div>
                        <span>Total completed rounds with this card</span>
                    </div>
                    <div className="filter">
                        <button onClick={() => {setFilter("rounds")}}>Rounds</button>
                        <button onClick={() => {setFilter("wins")}}>Wins</button>
                        <button onClick={() => {setFilter("losses")}}>Losses</button>
                    </div>
                    <Joker list={props.list} page={page} filter={filter}/>
                    </div>
                <div id='page'>
                    <button onClick={() => {decrementPage()}}>&lt;</button>
                    <span>{`Page ${page}/${pageLimit}`}</span>
                    <button onClick={() => {incrementPage()}}>&gt;</button>
                </div>
        </>
    else if(props.item == "hands" || props.item == "consumables" || props.item == "tarots" || props.item == "planets" || props.item == "spectrals" || props.item == "vouchers"){
        let keyMessage = "Number of times this card has been used"
        if(props.item == "vouchers")
            keyMessage = "Number of times this Voucher has been redeemed"
    
        if(props.item == "hands")
            return <>
            <div id="displayBox">
                <Other list={props.list} item={props.item} page={page}/>
                </div>
            </>
        return <>
            <div id="displayBox">
                <div className="key">
                        <div></div>
                        <span>{keyMessage}</span>
                </div>
                <Other list={props.list} item={props.item} page={page}/>
                </div>
            <div id='page'>
                    <button onClick={() => {decrementPage()}}>&lt;</button>
                    <span>{`Page ${page}/${pageLimit}`}</span>
                    <button onClick={() => {incrementPage()}} >&gt;</button>
            </div>
        </>
    } else {
        return <div id="displayBox"><p className="error">An error has occurred. Please reload the site.</p></div>
    }
}

export default DisplayList