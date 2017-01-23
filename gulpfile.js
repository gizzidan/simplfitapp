var gulp = require('gulp');
var cleanCSS = require('gulp-clean-css');
var uglify = require('gulp-uglify');

gulp.task('minify-css', function() {
  return gulp.src('simplfit2/assets/css/*.css')
    .pipe(cleanCSS())
    .pipe(gulp.dest('simplfit2/static'));
});

gulp.task('uglify', function() {
  return gulp.src('simplfit2/assets/js/*.js')
    .pipe(uglify())
    .pipe(gulp.dest('simplfit2/static'));
});

gulp.task('minify', ['minify-css', 'uglify']);
