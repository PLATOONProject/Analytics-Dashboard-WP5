import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  url:string = "http://localhost:8000/time_lines"
  constructor(private httpClient : HttpClient) { }
  getServices() {
    return this.httpClient.get(this.url, { responseType: 'text' });
  }
  getResults(){
    return this.httpClient.get(this.url,{responseType: 'text'});
  }
}
