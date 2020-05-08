import React from "react"
import { Link } from "gatsby"
import Card from "../components/buttons/card"
import CardCatalog from "../components/buttons/card-catalog"

const CatalogNavigation = () => {

  return(
    <div className="window" style={{ margin: '32px',
                                     width: '250px' }}>
      <div className="title-bar">
       <div className="title-bar-text">
         Library Catalog   
        </div>
      </div>
      <div className="window-body">
        <fieldset>
	    <a href="#" onClick="console.log(`Book`); return false"><img src="assets/img/address_book-0.png" /></a>
            <img src="assets/img/address_book_card.png" />
            <Card />
            <img src="assets/img/cardfile-1.png" />
            <CardCatalog />
	    <img src="assets/img/cd_audio_cd_a-0.png" alt="Music" />
            <img src="assets/img/movie_maker-1.png" alt="Video &amp; Movies" />
            <img src="assets/img/help_book_cool-0.png" />
         </fieldset>
       </div>
    </div>)
}

export default CatalogNavigation
