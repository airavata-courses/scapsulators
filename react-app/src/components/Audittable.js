import React from 'react';
// import 'react-bootstrap-table2-paginator/dist/react-bootstrap-table2-paginator.min.css'
// import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
// import 'bootstrap/dist/css/bootstrap.min.css';
import { TableData } from '../data/TableData';
import paginationFactory from 'react-bootstrap-table2-paginator';
import BootstrapTable from 'react-bootstrap-table-next';
import '../Homepage.css'


function Audittable({showModal, openModal}) {
  const columns = [{dataField: "id", text: "#"}, {dataField: "firstname", text: "First Name"}, {dataField: "lastname", text: "Last Name"}
  , {dataField: "username", text: "Username"}, {dataField: "laststation", text: "Station"}]
 
 
    const tableRowEvents = {
     onClick: (e, row, rowIndex) => {
       console.log(`clicked on row with index: ${rowIndex}`);
       openModal();
     }
  }
   


  return (
      <div style={table}>
          <p style={text}>Previous Data</p>
      <BootstrapTable hover keyField="id" data={TableData}  columns={columns} rowEvents={ tableRowEvents } pagination={paginationFactory({sizePerPage:5})}/>
      </div>
 );
}

export default Audittable;

const text = {fontWeight: 'bold'}

const table = {
    width: "30%",
    marginLeft:'30vh',
    marginTop:'10vh',
    color: 'white !important',
    background: 'white',
    border: 'black 1px solid',
    borderRadius: '10px',
    padding: '1rem',
    textAlign: 'center'
    
}

// function Etable(){
//   return (
//   <Table className="etable" striped bordered hover variant="dark" pagination={paginationFactory()}>
//  <thead>
//    <tr>
//      <th>#</th>
//      <th>First Name</th>
//      <th>Last Name</th>
//      <th>Username</th>
//      <th>Last Station</th>
//    </tr>
//  </thead>
//  <tbody>
//    {TableData.map((item,index) => {
//      return (
//        <tr key={index+1}>
//      <td>{index+1}</td>
//      <td>{item.firstname}</td>
//      <td>{item.lastname}</td>
//      <td>{item.username}</td>
//      <td>{item.laststation}</td>
//    </tr>
//      );
//    })}
   
//  </tbody>
// </Table>);
// }
