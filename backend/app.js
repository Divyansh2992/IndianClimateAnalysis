const express=require("express");
const cors = require("cors");
const app=express();
const fs = require('fs');
const path = require('path');
const epwRoutes = require('./routes/epw');

// Enable CORS for all origins
app.use(cors());
app.use(express.json());
app.use('/api/epw', epwRoutes);

app.listen(3000,()=>{
    console.log("Server is listening on port 3000");
})