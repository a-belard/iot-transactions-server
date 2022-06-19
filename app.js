import express, { json, urlencoded } from "express";
import cors from "cors";
import { corsFunction } from "./utils/cors.js";
const app = express();
const PORT = 5050;

//routes
import transactsRouter from "./routes/transacts.route";

app.use(cors());
app.use(corsFunction);
app.use(
  json({
    limit: "5000mb",
  })
);
app.use(urlencoded({ extended: true }));

app.use(transactsRouter);

app.listen(process.env.PORT || PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});
