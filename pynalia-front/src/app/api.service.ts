import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from './../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  constructor(private httpClient : HttpClient) { }

  generatePlots(file_path_param, selectedDashboards_param){

    let httpHeaders = new HttpHeaders({
     'Content-Type' : 'application/json',
     'Access-Control-Allow-Origin':'*'
    });
    let options = {
         headers: httpHeaders
    };

    var object = {};
      object['file_path'] = file_path_param;
      object['selectedDashboards'] = selectedDashboards_param;
    console.log(object)
    return this.httpClient.post<Element[]>(environment.apiURL+ '/generate', JSON.stringify(object), options);
  }
}
