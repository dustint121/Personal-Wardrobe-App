import React, { useState, useEffect } from "react";
import axios from "axios";
import Grid from "@mui/material/Grid";
import ImageList from "@mui/material/ImageList";
import ImageListItem from "@mui/material/ImageListItem";
import Typography from "@mui/material/Typography";
import Paper from "@mui/material/Paper";

function App() {
  const [all_clothing, setClothing] = useState([]);

  useEffect(() => {
    fetchAllClothes().then((result) => {
        if (result) {
            setClothing(result);
        }
    });
}, []);


  async function fetchAllClothes() {
    const response = await axios.get("http://localhost:5000/clothes");
    console.log(response.data)
    return response.data;
 }



  return (
    <div className="App">
      <h1 style={{textAlign: 'center'}}>Clothing Pieces</h1>
      {/* Use Grid component to create a layout grid */}
      <Grid container spacing={2}>
        {/* Loop through the data array and render each item */}
        {all_clothing.map(item => (
          // Use Grid component to create a grid item with different column widths at different breakpoints
          <Grid item key={item.ID} xs={12} sm={6} md={4} lg={3} xl={2} >
            {/* Use Paper component to wrap each item with a box */}
            <Paper elevation={3} sx={{ p: 2 }}>
              {/* Use ImageList and ImageListItem components to display the image data */}
              <ImageList sx={{ width: "100%", height: "auto" }} cols={1} rowHeight="auto">
                <ImageListItem>
                  {/* Use src attribute to set the image source to "data:image/jpeg;base64," + imageData */}
                  <img src={"data:image/jpeg;base64," + item.Image_Data} alt={item.Short_Descriptor} loading="lazy" />
                </ImageListItem>
              </ImageList>
              {/* Use Typography component to display the text information */}
              <Typography variant="h6" gutterBottom>{item.Short_Descriptor}</Typography>
              <Typography variant="body1" gutterBottom>{item.Brand}</Typography>
              <Typography variant="body2" color="text.secondary">{item.Category}</Typography>
            </Paper>
          </Grid>
        ))}
      </Grid>
    </div>
  );
}




export default App;
