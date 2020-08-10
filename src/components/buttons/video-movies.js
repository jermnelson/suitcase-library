import React from "react"

import VideoAndMoviesIcon from "../../images/VideoAndMoviesIcon.png"

const VideoAndMovies = () => {

  const handleClick = () => {
   return (alert('Browse the Catalog'))

  }

  return(
   <button href="#" onClick={handleClick}>
     <img alt="Video and Movies" src={VideoAndMoviesIcon} /> 
   </button>
  )
}

export default VideoAndMovies 
