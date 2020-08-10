import React from "react"
import { Link } from "gatsby"
import Card from "../components/buttons/card"
import CardCatalog from "../components/buttons/card-catalog"
import MusicBrowser from "../components/buttons/music"
import VideoAndMovies from "../components/buttons/video-movies"
import ReferenceHelp from "../components/buttons/help"


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
            <Card />
            <CardCatalog />
            <MusicBrowser />
            <VideoAndMovies />
            <ReferenceHelp />
         </fieldset>
       </div>
    </div>)
}

export default CatalogNavigation
