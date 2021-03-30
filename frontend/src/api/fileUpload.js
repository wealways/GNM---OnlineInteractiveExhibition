import { createInstanceFile } from "./index.js";

const instance = createInstanceFile();

function fileUpload(artist, file, success, fail) {
    instance
        .post(`galleries/image/input/${artist}/`,file)
        .then(success)
        .catch(fail);
}

export {fileUpload};
