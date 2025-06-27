import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  standalone: false
})
export class RegisterComponent {
  email: string = '';
  password: string = '';
  message: string = '';
  error: string = '';

  constructor(private auth: AuthService, private router: Router) {
  }
  register() {
    this.auth.register({ email: this.email, password: this.password }).subscribe({
      next: () => {
        this.message = 'Registered!';
        this.router.navigate(['/login']);
      },
      error: () => {
        this.error = 'Error Occured !';
      }
    });
  }
}
