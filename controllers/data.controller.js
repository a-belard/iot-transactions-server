export const addTransact = async (req, res) => {
  try {
    let data = [];
    req.body.map((dt) => {
      dt = JSON.stringify(dt);
      data.push(dt.replace(/[{}]/g, "").replace(/[""]/g, ""));
    });
    console.warn("Uploaded successfully");
    return res.json({ message: "Uploaded successfully", data, status: 200 });
  } catch (ex) {
    res.status(400).send({ message: "Failed uploading", err: ex.message });
  }
};
