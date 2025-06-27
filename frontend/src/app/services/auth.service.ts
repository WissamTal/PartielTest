import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = 'http://localhost:5000/api';
  constructor(private http: HttpClient, private router: Router) { }

  register(user: { email: string, password: string }) {
    return this.http.post(`${this.apiUrl}/register`, user);
  }
  login(credentials: { email: string, password: string }) {
    return this.http.post<{ access_token: string}>(`${this.apiUrl}/login`, credentials);
  }
  saveToken(token: string) {
    localStorage.setItem('access_token', token);
  }
  logout() {
    localStorage.removeItem('access_token');
    this.router.navigate(['/login']);
  }
  isLoggedIn():boolean {
    return !!localStorage.getItem('access_token');
  }
}
