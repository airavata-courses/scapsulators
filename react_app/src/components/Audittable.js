import React, {useState, useEffect} from 'react';
// import 'react-bootstrap-table2-paginator/dist/react-bootstrap-table2-paginator.min.css'
// import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
// import 'bootstrap/dist/css/bootstrap.min.css';

import paginationFactory from 'react-bootstrap-table2-paginator';
import BootstrapTable from 'react-bootstrap-table-next';
import '../Homepage.css'
import axios from 'axios';
import { getData} from '../api/image';
import { url } from '../config';
import { getCookie } from '../services/cookies';


function Audittable({showModal, openModal, setLoading, setData}) {
  const [tdata, setTdata] = useState([]);
  const userDetails = getCookie();
  console.log(userDetails.email);
  var data = JSON.stringify({"username":userDetails.email});

var config = {
  method: 'post',
  url: `http://${url}/api/getaudit`,
  headers: { 
    'Content-Type': 'application/json',
    'Authorization': userDetails.accessToken
  },
  data: data
};

  
  useEffect(async () => {
    axios(config)
.then(function (response) {
  console.log(response);
  if(response.data.status === 200) {
    
    setTdata(response.data.data);

  }
}).catch(function (error) {
    console.log(error);
});
    
  }, []);
  

  const columns = [{dataField: "index", text: "#"}, {dataField: "date", text: "Date Time"}, {dataField: "nexradStation", text: "NexRad Station"}, {dataField: "Visualization", text: "Visualization"}, {dataField: "Link", text: "link"} ]
 
 
    const tableRowEvents = {
      
      onClick: async (e, row, rowIndex) => {
        openModal();
        const body = {visualize: row.Visualization , station: row.nexradStation , timestamp: row.date}

        console.log(body);
        var result = await getData(body, userDetails.email);

    if (result.success === true) {
      setLoading(false);
      setData(result.data);
    } 

    else{
      alert('Querry Failed! No data found, try some other date');
      openModal();
    }
       
       
     }
  }
   



  return (
      <div style={table}>
          <p style={text}>Previous Data</p>
      <BootstrapTable hover keyField="id" data={tdata}  columns={columns} rowEvents={ tableRowEvents } pagination={paginationFactory({sizePerPage:5})}/>
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
