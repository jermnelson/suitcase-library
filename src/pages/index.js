import React from "react"
import { Link } from "gatsby"

import Layout from "../components/layout"

const Home = () => {
  
  return (
   <Layout>
      <div className="wrapper">
       <h1>Bug-Out Library</h1> 
       <a href="https://learn.sparkfun.com/tutorials/rfid-beginners-tutorial">RFID Beginners Tutorial</a>
      </div>
   </Layout>
  )
}

export default Home
