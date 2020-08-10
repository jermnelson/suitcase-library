import React from "react"
import AikiGardener from './aiki-gardener'
import Cataloger from './cataloger'
import HeadLibrarian from './head-librarian'
import SysAdmin from './sys-admin'
import { Link } from "gatsby"

import Layout from "../../components/layout"

const Staff = () => {
  
  return (
   <Layout>
      <div className="wrapper">
       <h1>Staff</h1>
       <HeadLibrarian />
       <Cataloger />
       <AikiGardener />
       <SysAdmin />
      </div>
   </Layout>
  )
}

export default Staff
