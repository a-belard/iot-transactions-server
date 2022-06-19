import express from "express";
import { addTransact } from "../controllers/data.controller.js";
const router = express.Router();

router.post("/transaction", addTransact);

export default router;
