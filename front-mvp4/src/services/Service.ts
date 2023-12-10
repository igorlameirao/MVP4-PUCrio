import { api } from './_base'
// import axios, { AxiosInstance } from 'axios';


export class Service {
    private nomeController = "machine";

    public Submit(data: any) {
        return api.post(`${this.nomeController}`, data);
    }
}

