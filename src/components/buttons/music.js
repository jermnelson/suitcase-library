import React from "react"

import MusicCD from "../../images/CompactDiscAudio.png"

const MusicBrowser = () => {

  const handleClick = () => {
   return (alert('Browse the Catalog'))

  }

  return(
   <button href="#" onClick={handleClick}>
     <img alt="Audio Compact Disc (CD)" src={MusicCD} /> 
   </button>
  )
}

export default MusicBrowser
