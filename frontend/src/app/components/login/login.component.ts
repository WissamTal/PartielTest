import { Component} from '@angular/core';
import {AuthService} from '../../services/auth.service';
import { Router } from '@angular/router';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  standalone: false
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  error: string = '';

  constructor(private auth: AuthService, private router: Router) { }

  login() {
    this.auth.login({ email: this.email, password: this.password }).subscribe({
      next: (res) => {
        this.auth.saveToken(res.access_token);
        this.router.navigate(['/films']);
      },
     error: () => {
        this.error = 'login failed';
     }
    });
  }

}
