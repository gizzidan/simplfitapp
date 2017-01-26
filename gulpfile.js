var gulp = require('gulp');
var cleanCSS = require('gulp-clean-css');
var uglify = require('gulp-uglify');

gulp.task('minify-css', function() {
  return gulp.src([
    '/Users/gizzidan/virtualenvs/simplfit2/assets/css/*.css',
    '/Users/gizzidan/virtualenvs/simplfit2/*/static/css/*.css'
  ])
    .pipe(cleanCSS())
    .pipe(gulp.dest('/Users/gizzidan/virtualenvs/simplfit2/build/css'));
});

gulp.task('uglify', function() {
  return gulp.src([
    '/Users/gizzidan/virtualenvs/simplfit2/assets/*/*.js',
    '/Users/gizzidan/virtualenvs/simplfit2/*/static/js/*.js'
  ])
    .pipe(uglify())
    .pipe(gulp.dest('/Users/gizzidan/virtualenvs/simplfit2/build/js'));
});

gulp.task('minify', ['minify-css', 'uglify']);
