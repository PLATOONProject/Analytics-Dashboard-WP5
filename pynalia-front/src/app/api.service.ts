import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  baseUrl:string = "http://localhost:8000"
  constructor(private httpClient : HttpClient) { }

  generatePlots(selectedDashboards){
    console.log(selectedDashboards)
    //return this.httpClient.get(this.baseUrl+"generate",{responseType: 'text'});
    return this.httpClient.post<Element[]>(this.baseUrl + '/generate', selectedDashboards );
  }
}
