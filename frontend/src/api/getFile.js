import { createInstance } from "./index.js";

const instance = createInstance();

function getFile(artist, success, fail) {

    instance
        .post(`galleries/image/input/${artist}/`)
        .then(success)
        .catch(fail);
}

export {getFile};
